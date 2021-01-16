const MusicBrainzApi = require('musicbrainz-api').MusicBrainzApi;


const url = "https://musicbrainz.org/ws/2";

const mbApi = new MusicBrainzApi({
    appName: 'node-demo-app',
    appVersion: '0.1.0',
    appContactInfo: 'britzkopf@gmail.com',
    baseUrl: 'https://musicbrainz.org'
});

async function queryArtist(p, searchString) {

    await p.send(`
        add spinner to=results id=searchspinner label="search executing"
    `) 
    
    let query = {};
    query['artist'] = searchString;

    let returnData = await mbApi.searchArtist(query, 0, 10);

    let returnArray = returnData['artists'];
    console.log(returnArray);
    
    /* ? why doesn't this work ? 
    
    returnArray.forEach(async element => {
        await p.send(`
            add text value="${element.name}"
        `)
    });*/
    
    for (i=0; i < returnArray.length; i++) {
        await p.send(`
                    add text to=results value="${returnArray[i].name}"
        `)
    }
    await p.send(`
        remove results:searchspinner
    `)

}

async function queryAlbum(p, searchString) {

    await p.send(`
        add spinner to=results id=searchspinner label="search executing"
    `) 

    let query = {};
    query['release'] = searchString;

    let returnData = await mbApi.searchRelease(query, 0, 10);

    let returnArray = returnData['releases'];       
    console.log(returnArray);

    
    for (i=0; i < returnArray.length; i++) {
        await p.send(`
                    add text to=results value="${returnArray[i].title}"
        `)
    }
    await p.send(`
        remove results:searchspinner
    `)

}

module.exports = {
    queryArtist: queryArtist,
    queryAlbum: queryAlbum
}