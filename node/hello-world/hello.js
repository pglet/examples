const pglet = require("pglet");

(async () => {
    p = await pglet.page("hello");

    await p.send("clean");
    await p.send("add text value='Hello, world!'");
})();