import React from 'react';
import ReactLoading from 'react-loading';

const Loading = () => {
    return (
        <div style={{display: 'flex', justifyContent: 'center', marginTop: '200px'}}>
            <ReactLoading  height={'15%'} width={'15%'} color={'black'} type={'bubbles'} />
        </div>
    );
};

export default Loading;