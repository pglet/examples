const pglet = require("pglet");

(async () => {
    // test app
    await pglet.app("hello-app", async (p) => {

        await p.send("clean");
        await p.send("add text value='Hello, world!'");
    });

    process.stdin.resume();
})();