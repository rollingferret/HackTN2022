import React from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

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
                zoom={8}
                style={mapStyles}
                initialCenter={{ lat: lat, lng: long }}
            >
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
