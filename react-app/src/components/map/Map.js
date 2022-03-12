import React from 'react';
import { Map, GoogleApiWrapper, Marker, Circle } from 'google-maps-react';

const mapStyles = {
    width: '40%',
    height: '40%'
}

let key = process.env.REACT_APP_GOOGLEMAPS
// console.log(key)

let lat
let long

if(navigator.geolocation) {
    console.log("navigator.geolocation is available");
    navigator.geolocation.getCurrentPosition(function(position) {
      console.log("current position acquired");
      lat = Number(position.coords.latitude)
      long = Number(position.coords.longitude)


    });


}






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
                radius={1600}
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
                <Marker position={{ lat: 48.00, lng: -122.00 }} />
                <Marker position={{ lat: 39.00, lng: -120.00 }} />
            </Map>
            </>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: key
})(MapContainer);
