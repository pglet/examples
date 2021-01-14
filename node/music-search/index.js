#!/usr/bin/env node

const axios = require('axios');
const parser = require('minimist');
const MusicBrainzApi = require('musicbrainz-api').MusicBrainzApi;
const pglet = require('pglet');

const args = parser(process.argv.slice(2));

const url = "https://musicbrainz.org/ws/2";

const mbApi = new MusicBrainzApi({
    appName: 'node-demo-app',
    appVersion: '0.1.0',
    appContactInfo: 'britzkopf@gmail.com',
    baseUrl: 'https://musicbrainz.org'
});

let query = {};
let result = {};

if ('artist' in args) {

    query['artist'] = "'" + args['artist'] + "'";
    mbApi.searchArtist(query, 0, 10).then((returnData) => {
        Object.assign(result, returnData);
    })

}

if ('album' in args) {

    query['album'] = "'" + args['album'] + "'";
    mbApi.searchRelease(query, 0, 10).then((returnData) => {
        Object.assign(result, returnData);
    })

}

(async () => {
    
    let p = await pglet.page();
    await p.send(`
        add to=page at=0
        stack id=search width=400px horizontalAlign=stretch
          text value='Search MusicBrainz - The Open Music Encyclopedia'
          textbox id=string label='Search for...'
          dropdown id=dropdown label='By'
            option key=artist text=artist
            option key=release text=album
          button id=button primary text=Search data=search_btn

          
    `)
    let searchType;
    while(true) {
        const e = await p.waitEvent();
        // if (e._data == 'artists') {
        //     console.log('artist search');
        // }
        // if (e._data == 'releases') {
        //     console.log('album search');
        // }

        if (e._target == 'search:dropdown') {
            searchType = e._data;
        }

        if (e._target == 'search:button') {
            let searchString = await p.send(`
                get search:string value 
            `)
            
            query[searchType] = searchString;
            let returnData = (searchType == 'artist') ? await mbApi.searchArtist(query, 0, 10) : await mbApi.searchRelease(query, 0, 10);
            Object.assign(result, returnData);
            let returnArray = result[(searchType + 's')];
            
            //console.log(returnArray);
            
            // returnArray.forEach(async element => {
            //     await p.send(`
            //         add text value="${element.name}"
            //     `)
            // });
            for (i=0; i < returnArray.length; i++) {
                await p.send(`
                         add text value="${returnArray[i].name}"
                `)
            }
        }

        // console.log(result);
        // console.log('\n\n\n\n');
        // console.log(result[(searchType+'s')]);
        // result[(searchType + 's')].foreach(async element => {
        //     await p.send(`
        //         add to=page at=1
        //         text value=${element.name}
        //     `)
        // });

        console.log(e);
    }

})();


