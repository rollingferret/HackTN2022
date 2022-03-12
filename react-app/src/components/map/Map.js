import React from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

const mapStyles = {
    width: '40%',
    height: '40%'
}

export class MapContainer extends React.Component {

    render() {
        return (
            <Map
                google={this.props.google}
                zoom={8}
                style={mapStyles}
                initialCenter={{ lat: 47.444, lng: -122.176 }}
            >
                <Marker position={{ lat: 48.00, lng: -122.00 }} />
                <Marker position={{ lat: 39.00, lng: -120.00 }} />
            </Map>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyBmW2VGroK49j2DSFbwPqskiZb69CgDX-c'
})(MapContainer);
