export class Map{

    constructor(longitude,latitude) {
        this.long = longitude;
        this.lat = latitude;
        this.zoom = 6;
        this.id_counter = 0;
        this.mapID = "";
    }
    
    init_map(map_id){
        L.mapbox.accessToken = 'pk.eyJ1IjoiYmxhbmt4eCIsImEiOiJja3A1bm40bjYwaWs5MnRxdHdua2JiazNyIn0.iFNN7eAz04uWKAazMhjHQQ';
        const map = L.mapbox.map(map_id).setView([this.long, this.lat], this.zoom)
        const marker = L.mapbox.Marker([this.long,this.lat]).addTo(map)
            
    }
    add_map(){
        const map_div = document.createElement("div");
        this.id_counter += 1
        this.mapID.concat("map", this.id_counter)
        map_div.setAttribute("id", this.mapID)
        console.log(this.mapID)
        this.init_map(this.long , this.lat, this.mapID)
        $("#all-chatbox").appendChild(map_div)


    }
    
}
