# Todo app in Javascript using Pglet


The script requires npm and Typescript to be installed globally

    npm install -g typescript

In order to overcome rate limits of Github API when not authenticated you will need a [personal token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) (scope is unimportant). 

Run the script with your personal token as follows:

    .\download-pglet-node.ps1 -token 123455678909087654321

This downloads and compiles the pglet-node library to this todo app's folder.

Then you can run `node app.js`