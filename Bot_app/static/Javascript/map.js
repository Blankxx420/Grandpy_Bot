
export class Map{

    constructor(longitude,latitude){
        this.long = longitude;
        this.lat = latitude;
        this.zoom = 6;
        this.init_map()

    }

    init_map(){
        mapboxgl.accessToken = 'pk.eyJ1IjoiYmxhbmt4eCIsImEiOiJja3A1bmtyejcyaTk0MnltY3g5ZjNqNGFwIn0.VXk6UtX9Ht11FuDPeV4lug';
        const map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/streets-v11', // style URL
            center: [this.long, this.lat], // starting position [lng, lat]
            zoom: this.zoom // starting zoom
        });

        // adding a marker according to coordinates
        const marker = new mapboxgl.Marker()
            .setLngLat([this.long, this.lat])
            .addTo(map);
    }
}
