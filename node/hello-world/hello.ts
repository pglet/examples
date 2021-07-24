import pglet from "pglet";

(async () => {
    let p = await pglet.page();
    await p.add(new pglet.Text({value: "Hello, world!"}));
})();