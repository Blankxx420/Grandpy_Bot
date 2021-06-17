export class Map{

    constructor(longitude,latitude){
        this.long = longitude;
        this.lat = latitude;
        this.zoom = 6;
    }
    
    init_map(){
        mapboxgl.accessToken = 'pk.eyJ1IjoiYmxhbmt4eCIsImEiOiJja3A1bm40bjYwaWs5MnRxdHdua2JiazNyIn0.iFNN7eAz04uWKAazMhjHQQ';
        var map = new mapboxgl.Map({
            container: "map",
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [this.long, this.lat],
            zoom: this.zoom,
        })
        var marker = new mapboxgl.Marker()
                .setLngLat([this.long, this.lat])
                .addTo(map)
            
    }

    
}; 
