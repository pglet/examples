const pglet = require("pglet");

(async () => {

    // start a new session for every user visit
    await pglet.app("greeter-app", async (p) => {

        // add textbox and a button
        let txt_name = await p.send("add textbox label='Your name' description='Please provide your full name'");
        let btn_hello = await p.send("add button primary text='Say hello'");
        
        while(true) {
            // wait until button is clicked
            const e = await p.waitEvent();
            if (e.target === btn_hello && e.name === 'click') {

                // get the entered value of a textbox
                let name = await p.send(`get ${txt_name} value`);

                // clean the page and output the greeting
                await p.send("clean page");
                await p.send(`add text value='Hello, ${name}!'`);
            }
        }
    });

    process.stdin.resume();
})();
