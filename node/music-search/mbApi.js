const MusicBrainzApi = require('musicbrainz-api').MusicBrainzApi;


const url = "https://musicbrainz.org/ws/2";

const mbApi = new MusicBrainzApi({
    appName: 'node-demo-app',
    appVersion: '0.1.0',
    appContactInfo: 'britzkopf@gmail.com',
    baseUrl: 'https://musicbrainz.org'
});

async function queryArtists(p, searchString) {

    await p.send(`
        add spinner to=results at=0 id=searchspinner label="search executing"
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


    await p.send(`
        add detailslist id=resultsList to=results 
            listColumn key="name" value="name"
            listColumn key="type" value="type"
    `)
    for (i=0; i < returnArray.length; i++) {
        await p.send(`
         add to=resultsList 
                listItem key="${returnArray[i].name}" value="${returnArray[i].name}" type="${returnArray[i].type}"

        `)
        // await p.send(`
        //     add text to=results value="${returnArray[i].name}"
        // `)
    }
    await p.send(`
        remove results:searchspinner
    `)

}

async function queryAlbums(p, searchString) {

    await p.send(`
        add spinner to=results id=searchspinner label="search executing"
    `) 

    let query = {};
    query['release-group'] = searchString;

    let returnData = await mbApi.searchReleaseGroup(query, 0, 10);
    console.log(returnData);
    let returnArray = returnData['release-groups'];       
    console.log(returnArray);

    
    for (i=0; i < returnArray.length; i++) {
        // let album = await queryAlbum(returnArray[i].id);
        // console.log("....album.....");
        // console.log(album);
        await p.send(`
                    add text to=results value="ALBUM:${returnArray[i].title} ARTIST:${returnArray[i]['artist-credit'][0].artist.name} RELEASE:${returnArray[i]['first-release-date']}"
        `)
    }
    await p.send(`
        remove results:searchspinner
    `)

}

async function queryAlbum(id) {

    const release = await mbApi.getReleaseGroup(id, ['artists']);
    return release;

}

module.exports = {
    queryArtists: queryArtists,
    queryAlbums: queryAlbums
}