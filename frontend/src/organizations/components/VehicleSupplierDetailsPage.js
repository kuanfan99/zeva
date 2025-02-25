import React from 'react';
import PropTypes from 'prop-types';

import Button from '../../app/components/Button';
import Loading from '../../app/components/Loading';
import CustomPropTypes from '../../app/utilities/props';
import ROUTES_ORGANIZATIONS from '../../app/routes/Organizations';
import VehicleSupplierClass from './VehicleSupplierClass';
import formatNumeric from '../../app/utilities/formatNumeric';

const VehicleSupplierDetailsPage = (props) => {
  const {
    details,
    editButton,
    handleInputChange,
    handleSubmit,
    inputLDVSales,
    ldvSales,
    loading,
    locationState,
    modelYears,
    selectedModelYear,
    handleDeleteSale,
  } = props;
  const { organizationAddress } = details;

  if (loading) {
    return <Loading />;
  }

  return (
    <div id="vehicle-supplier-details" className="page">
      <div className="row mt-3">
        <div className="col">
          <h2 className="mb-2">Vehicle Supplier Information</h2>
          <div className="mt-3">
            <h4 className="d-inline">Legal Name: </h4>
            <span> {details.name} </span>
          </div>

          <div className="mt-3">
            <h4 className="d-inline">Common Name: </h4>
            <span> {details.shortName} </span>
          </div>

          <div className="mt-3">
            <h4 className="d-inline">Status: </h4>
            <span> {(details.isActive) ? 'Actively supplying vehicles in British Columbia' : 'Not actively supplying vehicles in British Columbia'} </span>
          </div>

          <div className="row">
            <div className="d-inline-block col-5 mr-5 mt-3">
              <h4>Service Address</h4>
              {organizationAddress
              && organizationAddress.map((address) => (
                address.addressType.addressType === 'Service' && (
                  <div key={address.id}>
                    {address.representativeName && (
                      <div> {address.representativeName} </div>
                    )}
                    <div> {address.addressLine1} </div>
                    <div> {address.addressLine2} </div>
                    <div> {address.city} {address.state} {address.country} </div>
                    <div> {address.postalCode} </div>
                  </div>
                )
              ))}
            </div>
            <div className="d-inline-block col-5 mt-3">
              <h4>Records Address</h4>
              {organizationAddress
              && organizationAddress.map((address) => (
                address.addressType.addressType === 'Records' && (
                  <div key={address.id}>
                    {address.representativeName && (
                      <div> {address.representativeName} </div>
                    )}
                    <div> {address.addressLine1} </div>
                    <div> {address.addressLine2} </div>
                    <div> {address.city} {address.state} {address.country} </div>
                    <div> {address.postalCode} </div>
                  </div>
                )
              ))}
            </div>
          </div>

          <div className="mt-3">
            <h4 className="d-inline">Vehicle Supplier Class: </h4>
            <span> <VehicleSupplierClass supplierClass={details.supplierClass} /> </span>
          </div>

          <div className="mt-3">
            <h4 className="d-inline">3 Year Average LDV Sales: </h4>
            <span> {formatNumeric(Math.round(details.avgLdvSales), 0)} </span>
          </div>

          <div className="mt-3">
            {!details.hasSubmittedReport && (
              <div className="mb-2">Enter the previous 3 year LDV sales total to determine vehicle supplier class.</div>
            )}
            {details.hasSubmittedReport && (
            <h4 className="d-inline">Previous 3 Year LDV Sales: </h4>
            )}
            <form onSubmit={handleSubmit}>
              <div className="ldv-sales">
                {!details.hasSubmittedReport && (
                <div className="header-bg">
                  <div className="d-inline-block">
                    <select
                      className="form-control"
                      id="model-year"
                      name="modelYear"
                      onChange={handleInputChange}
                      value={selectedModelYear}
                    >
                      <option> </option>
                      {modelYears.map((modelYear) => (
                        <option key={modelYear.name} value={modelYear.name}>{modelYear.name}</option>
                      ))}
                    </select>
                  </div>
                  <div className="d-inline-block">
                    <input
                      className="form-control"
                      name="ldvSales"
                      onChange={handleInputChange}
                      type="text"
                      value={inputLDVSales}
                    />
                  </div>
                  <div className="d-inline-block">
                    <button
                      className="btn button primary"
                      type="submit"
                    >
                      Add
                    </button>
                  </div>
                </div>
                )}

                <ul className="mb-0 mt-3">
                  {ldvSales.map((sale) => (
                    <li className="form-row my-2" key={sale.id}>
                      <div className="col-5 model-year">
                        {sale.modelYear} Model Year:
                      </div>
                      <div className="col-6 sales">
                        {formatNumeric(sale.ldvSales, 0)}
                      </div>
                      {!details.hasSubmittedReport && (
                        <div className="col-1 delete">
                          <button
                            onClick={() => {
                              handleDeleteSale(sale);
                            }}
                            type="button"
                          >
                            x
                          </button>
                        </div>
                      )}
                    </li>
                  ))}
                </ul>
              </div>
            </form>
          </div>
        </div>
        <div className="col-sm-2">
          {editButton}
        </div>
      </div>

      <div className="row">
        <div className="col-12">
          <div className="action-bar">
            <span className="left-content">
              <Button
                buttonType="back"
                locationRoute={ROUTES_ORGANIZATIONS.LIST}
                locationState={locationState}
              />
            </span>
            <span className="right-content" />
          </div>
        </div>
      </div>
    </div>
  );
};

VehicleSupplierDetailsPage.defaultProps = {
  inputLDVSales: '',
  locationState: undefined,
  selectedModelYear: '',
};

VehicleSupplierDetailsPage.propTypes = {
  details: CustomPropTypes.organizationDetails.isRequired,
  editButton: PropTypes.shape().isRequired,
  ldvSales: PropTypes.arrayOf(PropTypes.shape()).isRequired,
  loading: PropTypes.bool.isRequired,
  locationState: PropTypes.arrayOf(PropTypes.shape()),
  modelYears: PropTypes.arrayOf(PropTypes.shape()).isRequired,
  handleDeleteSale: PropTypes.func.isRequired,
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  inputLDVSales: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number,
  ]),
  selectedModelYear: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number,
  ]),
};

export default VehicleSupplierDetailsPage;
