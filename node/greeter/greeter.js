const pglet = require("pglet");

(async () => {
    let p = await pglet.page("greeter");

    let txt_name = await p.send("add textbox label='Your name' description='Please provide your full name'");
    let btn_hello = await p.send("add button primary text='Say hello'");
    
    while(true) {
        const e = await p.waitEvent();
        if (e.target === btn_hello && e.name === 'click') {
            let name = await p.send(`get ${txt_name} value`);
            await p.send("clean page");
            await p.send(`add text value='Hello, ${name}!'`);
        }
    }
})();

