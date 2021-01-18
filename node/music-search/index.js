#!/usr/bin/env node

const axios = require('axios');
const parser = require('minimist');
const MusicBrainzApi = require('musicbrainz-api').MusicBrainzApi;
const pglet = require('pglet');
const mbApi = require('./mbApi.js');


const args = parser(process.argv.slice(2));

// const url = "https://musicbrainz.org/ws/2";

// const mbApi = new MusicBrainzApi({
//     appName: 'node-demo-app',
//     appVersion: '0.1.0',
//     appContactInfo: 'britzkopf@gmail.com',
//     baseUrl: 'https://musicbrainz.org'
// });

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
        add to=page at=0 text size=large bold=true value='Search MusicBrainz - The Open Music Encyclopedia' margin="1em 0em"
    `)

    await p.send(`
        add to=page at=1
        stack id=search width=100% horizontal=true horizontalAlign=center 
          textbox id=string label='Search for...' width=400px
          dropdown id=dropdown label='By' width=200px
            option key=artist text=artist
            option key=release text=album
          button id=button primary text=Search data=search_btn width=100px margin=2em        
    `)

    await p.send(`
        add to=page at=2
        text size=medium bold=true value='Search Results'
        stack id=results width=100%      
    `)

    let searchType;
    while(true) {
        const e = await p.waitEvent();

        if (e._target == 'search:dropdown') {
            searchType = e._data;
        }

        if (e._target == 'search:button' && searchType == 'artist') {
            let searchString = await p.send(`
                get search:string value 
            `)
            await mbApi.queryArtists(p, searchString)          
        }

        if (e._target == 'search:button' && searchType == 'release') {
            let searchString = await p.send(`
                get search:string value 
            `)
            await mbApi.queryAlbums(p, searchString)            
        }

        console.log(e);
    }

})();


