import React from 'react';

import DateRangePicker from 'react-bootstrap-daterangepicker';

import 'bootstrap-daterangepicker/daterangepicker.css';
const MyDateRangePicker = () => {
    return (
            <DateRangePicker initialSettings={{ startDate: '2020-01-01', endDate: '2050-01-01', autoApply: true, locale: {
      format: 'YYYY-MM-DD'
    } }}>
                 <input type="text" className="black bold font_20" style={{height: '45px', marginRight: '20px', textAlign: 'center'}}/>
            </DateRangePicker>
    );
};

export default MyDateRangePicker;