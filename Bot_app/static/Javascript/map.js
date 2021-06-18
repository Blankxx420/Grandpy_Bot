export class Map{

    constructor(longitude,latitude) {
        this.long = longitude;
        this.lat = latitude;
        this.zoom = 6;
        this.id_counter = 0
    }
    
    init_map(mapID){
        L.mapbox.accessToken = 'pk.eyJ1IjoiYmxhbmt4eCIsImEiOiJja3A1bm40bjYwaWs5MnRxdHdua2JiazNyIn0.iFNN7eAz04uWKAazMhjHQQ';
        const map = L.mapbox.map('mapID').setView([this.long, this.lat], this.zoom)
        const marker = L.mapbox.Marker([this.long,this.lat]).addTo(map)
            
    }
    add_map(){
        let mapID = "";
        const map_div = document.createElement("div");
        this.id_counter += 1
        mapID.concat("map", this.id_counter)
        map_div.setAttribute("id", mapID)
        this.init_map(this.long , this.lat, mapID)
        $("#all-chatbox").appendChild(map_div)


    }
    
}
