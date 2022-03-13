import React from 'react';
import { Map, GoogleApiWrapper, Marker, Circle } from 'google-maps-react';

const mapStyles = {
    width: '40%',
    height: '40%'
}

let key = process.env.REACT_APP_GOOGLEMAPS
// console.log(key)

let lat = 36.1627
let long = -86.7816

if(navigator.geolocation) {
    console.log("navigator.geolocation is available");
    navigator.geolocation.getCurrentPosition(function(position) {
      console.log("current position acquired");
      lat = Number(position.coords.latitude)
      long = Number(position.coords.longitude)
      console.log(lat, long)


    });


}

let coords = { test: [39.7275, -104.8791] }





export class MapContainer extends React.Component {




    render() {
        return (
            <>

            <div>{lat} {long}</div>
            <Map
                google={this.props.google}
                zoom={13}
                style={mapStyles}
                initialCenter={{ lat: lat, lng: long }}
            >
            <Circle
                radius={1200}
                center={{ lat: lat, lng: long }}
                onMouseover={() => console.log('mouseover')}
                onClick={() => console.log('click')}
                onMouseout={() => console.log('mouseout')}
                strokeColor='transparent'
                strokeOpacity={0}
                strokeWeight={5}
                fillColor='#FF0000'
                fillOpacity={0.2}
            />
                {/* <Marker position={{ lat: 39.7275, lng: -104.8791 }} /> */}
                {
                    Object.values(coords).map((coords) => {
                        return <Marker position={{ lat: coords[0], lng: coords[1]}}/>
                    })
                }
            </Map>
            </>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: key
})(MapContainer);
