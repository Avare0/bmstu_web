import React from 'react';
import SimpleImageSlider from "react-simple-image-slider";

const ImageSlider = ({images}) => {

    let res = [];
    for(let i = 0; i < images.length; i++)
        res.push({url: window.static_url + images[i].photo});
    console.log(res);
    return (
    <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-around'}}>
      <SimpleImageSlider
        width={1100}
        height={504}
        style={{textAlign:'center'}}
        images={res}
        showBullets={false}
        showNavs={true}
      />
    </div>
  );
};

export default ImageSlider;