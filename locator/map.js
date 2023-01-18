let map;
let featureLayer;

function initMap() {
    const myLatLng = {lat: 50.95, lng: 8.77};
    var map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 6,
        mapId: "198c060214ce823", // You need to create your own map ID
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map:map,
        label: "A",
        title: "This Position is important!"
    });
    marker.setMap(map);

    var infoWindow = new google.maps.InfoWindow({
        content:"This is more information about this place</p>"
    });
    infoWindow.open(map, marker);

    featureLayer = map.getFeatureLayer("ADMINISTRATIVE_AREA_LEVEL_2");

    // Define the styling options
    const featureStyleOptions = {
        strokeColor: "#810FCB",
        strokeOpacity: 2.1,
        strokeWeight: 2.1,
        fillColor: "#810FCB",                      
        fillOpacity: 0.5,
    };

    // Apply the style to a single boundary.
    featureLayer.style = (options) => {
        //if (options.feature.placeId == "ChIJa76xwh5ymkcRW-WRjmtd6HU") {
        if (options.feature.placeId == "ChIJ5S-raZElv0cRoOwpSvxgJwM-WRjmtd6HU") { // Köln
        //if (options.feature.placeId == "ChIJ0zQtYiWsVHkRk8lRoB1RNPo") { // Hawai

        // Above Place ID is Switzerland
        return featureStyleOptions;
        }
    };
}
  window.initMap = initMap;