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

var query = {};
var result = {};

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

    //const searchDropdown = await p.send("add stack id=query");
    await p.send("add text id=query value=\"Search by \"");
    await p.send("add dropdown id=query value=artist");

    await p.send("add textbox id=query");

    while(true) {
        const e = await p.waitEvent();
        console.log(e);
    }

})();

// pglet.page().then((con) => {
//     con.send("add textbox id=query").then(() => {
//         while(true) {
//             con.waitEvent().then((e) => {
//                 console.log(e);
//             });
            
//         }
//     });
    
// });
