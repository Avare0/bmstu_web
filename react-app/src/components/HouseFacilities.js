import React from 'react';

const HouseFacilities = ({facilities}) => {
    return (
        <div>
            <div className="facilities">
                        {facilities.map(facility =>
                            <div className="facility" key={facility.facility.id}>
                                    <div className="facility_img">
                                        <img src={window.static_url + facility.facility.file} alt=""/>
                                    </div>
                                    <p>{facility.facility.name}</p>
                                </div>
                        )}

                    </div>
        </div>
    );
};

export default HouseFacilities;