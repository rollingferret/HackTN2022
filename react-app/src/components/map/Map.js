import React from 'react';
import css from './map.css';

let data = require('../../../src/site_data/formatted_daycares.json')

let key = process.env.REACT_APP_GOOGLEMAPS

let closeBy = []

function getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2) {
    var R = 6371; // Radius of the earth in km
    var dLat = deg2rad(lat2-lat1);  // deg2rad below
    var dLon = deg2rad(lon2-lon1); 
    var a = 
      Math.sin(dLat/2) * Math.sin(dLat/2) +
      Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
      Math.sin(dLon/2) * Math.sin(dLon/2)
      ; 
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    var d = R * c; // Distance in km
    return d;
  }
  
  function deg2rad(deg) {
    return deg * (Math.PI/180)
  }

  let lat = 36.174465
  let long = -86.767960

if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      let lat = Number(position.coords.latitude)
      let long = Number(position.coords.longitude)
    });
}

for (let item in data) {

    let left = data[item].coordinates.latitude
    let right = data[item].coordinates.longitude

    let distance = getDistanceFromLatLonInKm(left, right, lat, long)


    if (distance < 2) {


        data[item].distance = distance.toFixed(1)
        closeBy.push(data[item])

    }


}

closeBy.sort((a, b) => { return a.distance - b.distance })

const Map = () => {


    return (
        <>
            <div className='banner'></div>
            <div className='stopbeingbig'>
            {closeBy.map((arg) => {

                if (arg.star_rating === '/3') arg.star_rating = '0/3'

return <div className='test' key={arg.address}><div>Name: {arg.name}<br></br> Address: {arg.address}<br></br> County: {arg.county}<br></br> Rating: {arg.star_rating}<br></br> Distance:{arg.distance}</div></div>

})}
</div>
        </>
    );
}

export default Map
