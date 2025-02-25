"use strict";
const { OpenShiftClientX } = require("@bcgov/pipeline-cli");
const path = require("path");
const KeyCloakClient = require('./keycloak');

module.exports = settings => {
  const phases = settings.phases;
  const options = settings.options;
  const phase = options.env;
  const changeId = phases[phase].changeId;
  const oc = new OpenShiftClientX(Object.assign({namespace: phases[phase].namespace}, options));

  //add Valid Redirect URIs for the pull request to keycloak
  if(phase === 'dev') {
    const kc = new KeyCloakClient(settings, oc);
    kc.addUris();
  }

  const templatesLocalBaseUrl = oc.toFileUrl(path.resolve(__dirname, "../../openshift"));
  var objects = [];

  // The deployment of your cool app goes here ▼▼▼

  //create network security policies for internal pod to pod communications
  if(phase === 'dev') {
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/knp/knp-env-pr.yaml`, {
      'param': {
        'SUFFIX': phases[phase].suffix,
        'ENVIRONMENT': phases[phase].phase
      }
    }))
  }

  // create configs
  if(phase === 'dev') {
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/config/configmap.yaml`, {
      'param': {
        'NAME': phases[phase].name,
        'SUFFIX': phases[phase].suffix,
        'ENV_NAME': phases[phase].phase,
        'HOST_NAME': phases[phase].host,
        'BACKEND_HOST_NAME': phases[phase].backendHost,
        'SSO_NAME': phases[phase].ssoName,
        'KEYCLOAK_REALM': 'rzh2zkjq',
        'DJANGO_DEBUG': phases[phase].djangoDebug,
        'OCP_NAME': phases[phase].ocpName,
        'LOGOUT_HOST_NAME': phases[phase].logoutHostName,
      }
    }))
  }

  if(phase === 'dev') {
    //deploy Patroni required secrets
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/patroni/deployment-prereq.yaml`, {
      'param': {
        'NAME': 'patroni',
        'SUFFIX': phases[phase].suffix
      }
    }))
    //deploy Patroni
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/patroni/deployment.yaml`, {
      'param': {
        'NAME': 'patroni',
        'ENV_NAME': phases[phase].phase,
        'SUFFIX': phases[phase].suffix,
        'CPU_REQUEST': phases[phase].patroniCpuRequest,
        'CPU_LIMIT': phases[phase].patroniCpuLimit,
        'MEMORY_REQUEST': phases[phase].patroniMemoryRequest,
        'MEMORY_LIMIT': phases[phase].patroniMemoryLimit,
        'IMAGE_REGISTRY': 'image-registry.openshift-image-registry.svc:5000',
        'IMAGE_STREAM_NAMESPACE': phases[phase].namespace,
        'IMAGE_STREAM_TAG': 'patroni:v10-stable',
        'REPLICA': phases[phase].patroniReplica,
        'PVC_SIZE': phases[phase].patroniPvcSize,
        'STORAGE_CLASS': phases[phase].storageClass
      }
    }))
  }
  
  //only deploy rabbitmq secret and configmap
  if(phase === 'dev') {
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/rabbitmq/rabbitmq-secret-configmap-only.yaml`, {
      'param': {
        'NAME': phases[phase].name,
        'ENV_NAME': phases[phase].phase,
        'SUFFIX': phases[phase].suffix,
        'NAMESPACE': phases[phase].namespace,
        'CLUSTER_NAME': 'rabbitmq-cluster'
      }
    }))
  }

  // deploy frontend configmap
  //if(phase === 'dev') {
  //add CREDIT_AGREEMENTS_ENABLED for release-1.29.0
  objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/frontend/frontend-configmap.yaml`, {
    'param': {
      'NAME': phases[phase].name,
      'SUFFIX': phases[phase].suffix,
      'COMPLIANCE_REPORT_ENABLED': phases[phase].complianceReportEnabled,
      'COMPLIANCE_CALCULATOR_ENABLED': phases[phase].complianceCalculatorEnabled,
      'COMPLIANCE_RATIOS_ENABLED': phases[phase].complianceRatiosEnabled,
      'CREDIT_TRANSFERS_ENABLED': phases[phase].creditTransfersEnabled,
      'CREDIT_TRANSACTIONS_ENABLED': phases[phase].creditTransactionsEnabled,
      'INITIATIVE_AGREEMENTS_ENABLED': phases[phase].initiativeAgreementsEnabled,
      'MODEL_YEAR_REPORT_ENABLED': phases[phase].modelYearReportEnabled,
      'PURCHASE_REQUESTS_ENABLED': phases[phase].purchaseRequestsEnabled,
      'NOTIFICATIONS_ENABLED': phases[phase].notificationsEnabled,
      'ROLES_ENABLED': phases[phase].rolesEnabled,
      'CREDIT_AGREEMENTS_ENABLED': phases[phase].creditAgreementsEnabled
    }
  }))
  //}

  // deploy frontend
  objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/frontend/frontend-dc.yaml`, {
    'param': {
      'NAME': phases[phase].name,
      'SUFFIX': phases[phase].suffix,
      'VERSION': phases[phase].tag,
      'ENV_NAME': phases[phase].phase,
      'HOST_NAME': phases[phase].host,
      'CPU_REQUEST': phases[phase].frontendCpuRequest,
      'CPU_LIMIT': phases[phase].frontendCpuLimit,
      'MEMORY_REQUEST': phases[phase].frontendMemoryRequest,
      'MEMORY_LIMIT': phases[phase].frontendMemoryLimit,
      'REPLICAS':  phases[phase].frontendReplicas
    }
  }))

  //deploy backend
  objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/backend/backend-dc.yaml`, {
    'param': {
      'NAME': phases[phase].name,
      'SUFFIX': phases[phase].suffix,
      'VERSION': phases[phase].tag,
      'ENV_NAME': phases[phase].phase,
      'BACKEND_HOST_NAME': phases[phase].backendHost,
      'RABBITMQ_CLUSTER_NAME': 'rabbitmq-cluster',
      'CPU_REQUEST': phases[phase].backendCpuRequest,
      'CPU_LIMIT': phases[phase].backendCpuLimit,
      'MEMORY_REQUEST': phases[phase].backendMemoryRequest,
      'MEMORY_LIMIT': phases[phase].backendMemoryLimit,
      'HEALTH_CHECK_DELAY': phases[phase].backendHealthCheckDelay,
      'REPLICAS':  phases[phase].backendReplicas
    }
  })) 
  
  //deploy schemaspy
  if(phase === 'dev') {
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/schemaspy/schemaspy-dc.yaml`, {
      'param': {
        'SUFFIX': phases[phase].suffix,
        'ENV_NAME': phases[phase].phase,
        'CPU_REQUEST': phases[phase].schemaspyCpuRequest,
        'CPU_LIMIT': phases[phase].schemaspyCpuLimit,
        'MEMORY_REQUEST': phases[phase].schemaspyMemoryRequest,
        'MEMORY_LIMIT': phases[phase].schemaspyMemoryLimit,
        'HEALTH_CHECK_DELAY': phases[phase].schemaspyHealthCheckDelay,
        'OCP_NAME': phases[phase].ocpName
      }
    }))
  }

  /** 
  //deploy rabbitmq, use docker image directly
  //POST_START_SLEEP is harded coded in the rabbitmq template, replacement was not successful
  objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/rabbitmq/rabbitmq-cluster-dc.yaml`, {
    'param': {
      'NAME': phases[phase].name,
      'ENV_NAME': phases[phase].phase,
      'SUFFIX': phases[phase].suffix,
      'NAMESPACE': phases[phase].namespace,
      'CLUSTER_NAME': 'rabbitmq-cluster',
      'ISTAG': `image-registry.openshift-image-registry.svc:5000/${phases[phase].namespace}/rabbitmq:3.8.3-management`,
      'SERVICE_ACCOUNT': 'rabbitmq-discovery',
      'VOLUME_SIZE': phases[phase].rabbitmqPvcSize,
      'CPU_REQUEST': phases[phase].rabbitmqCpuRequest,
      'CPU_LIMIT': phases[phase].rabbitmqCpuLimit,
      'MEMORY_REQUEST': phases[phase].rabbitmqMemoryRequest,
      'MEMORY_LIMIT': phases[phase].rabbitmqMemoryLimit,
      'REPLICA': phases[phase].rabbitmqReplica,
      'POST_START_SLEEP': phases[phase].rabbitmqPostStartSleep,
      'STORAGE_CLASS': phases[phase].storageClass
    }
  }))
  */

  /*** remove minio deployment in pr pipeline, one pre-deployed minio will serve all prs
   * minio configurations stay in config.js unchanged
  objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/minio/minio-dc.yaml`, {
    'param': {
      'NAME': phases[phase].name,
      'SUFFIX': phases[phase].suffix,
      'ENV_NAME': phases[phase].phase,
      'PVC_SIZE': phases[phase].minioPvcSize,
      'CPU_REQUEST': phases[phase].minioCpuRequest,
      'CPU_LIMIT': phases[phase].minioCpuLimit,
      'MEMORY_REQUEST': phases[phase].minioMemoryRequest,
      'MEMORY_LIMIT': phases[phase].minioMemoryRequest      
    }
  }))
  */

  //add autoacaler
  /*****
  if(phase === 'test' || phase === 'prod') {
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/frontend/frontend-autoscaler.yaml`, {
      'param': {
        'NAME': phases[phase].name,
        'SUFFIX': phases[phase].suffix,
        'MIN_REPLICAS': phases[phase].frontendMinReplicas,
        'MAX_REPLICAS': phases[phase].frontendMaxReplicas
      }
    }))
    objects = objects.concat(oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/templates/backend/backend-autoscaler.yaml`, {
      'param': {
        'NAME': phases[phase].name,
        'SUFFIX': phases[phase].suffix,
        'MIN_REPLICAS': phases[phase].backendMinReplicas,
        'MAX_REPLICAS': phases[phase].backendMaxReplicas
      }
    }))
  }
  ********/

  oc.applyRecommendedLabels(
      objects,
      phases[phase].name,
      phase,
      `${changeId}`,
      phases[phase].instance,
  );
  oc.importImageStreams(objects, phases[phase].tag, phases.build.namespace, phases.build.tag);
  oc.applyAndDeploy(objects, phases[phase].instance);

};
