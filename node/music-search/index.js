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
    await p.send(`
        add to=page at=0
        stack width = 600px horizontalAlign=stretch
          text value='Search MusicBrainz - The Open Music Encyclopedia'
          dropdown id=searchBy label='Search'
            option key=artist text=artist
            option key=album text=album
    `)
    //await p.send("add text value=test");
    //await p.send("add stack id=query");
    //const response = await p.send("add to=query\n text id=test value=\"Search by \"");
    //console.log(response);

    //await p.send("add dropdown to=query value=artist");

    //await p.send("add textbox to=query");

    while(true) {
        const e = await p.waitEvent();
        console.log(e);
    }

})();
// add to=page at=0
// stack width=600px horizontalAlign=stretch
//   textbox id=fullName align=right value='someone' label=Name placeholder='Your name, please' description='That\'s your name'
//   textbox id=bio label='Bio' description='A few words about yourself' value='Line1\nLine2' multiline=true
//   dropdown id=color label='Your favorite color' placeholder='Select color'
//     option key=red text=Red
//     option key=green text=Green
//     option key=blue text=Blue
//   checkbox id=agree label='I agree to the terms of services'

// pglet.page().then((con) => {
//     con.send("add textbox id=query").then(() => {
//         while(true) {
//             con.waitEvent().then((e) => {
//                 console.log(e);
//             });
            
//         }
//     });
    
// });
