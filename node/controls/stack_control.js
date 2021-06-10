const pglet = require('../../../pglet-node/dist/index.js');

const Text = pglet.Text;
const Stack = pglet.Stack;
const Textbox = pglet.Textbox;
const Slider = pglet.Slider;
const Message = pglet.Message;

async function main(p) {

    p.title = "Stack example";
    p.horizontalAlign = "stretch";
    await p.update();

    const bgColor = "#ddddee";

    function items(count) {
        let items = [];
        for (const e of [...Array(count).keys()]) {
            items.push(new Text({value: e, align: "center", verticalAlign: "center", width: 30, height: 30, bgcolor: "CyanBlue10", color: "white", padding: 5}))
        }
        return items;
    }

    function createHorizontalStack(hAlign) {
        return new Stack({childControls: [
            new Text({value: hAlign}),
            new Stack({horizontal: true, horizontalAlign: hAlign, verticalAlign: "center", gap: 20, bgcolor: bgColor, childControls: [...items(3)]})
        ]})
    }

    function createVerticalStack(vAlign) {
        return new Stack({width: "20%", childControls: [
            new Text({value: vAlign}),
            new Stack({horizontalAlign: "center", verticalAlign: vAlign, height: 300, gap: 20, bgcolor: bgColor, childControls: [...items(3)]})
        ]})
    }
    let spacingStack = new Stack({horizontal: true, bgcolor: bgColor, gap: 0, childControls: [...items(5)]});
    console.log("spacingStack: ", spacingStack);
    function gapSliderChange(e) {
        spacingStack.gap = parseInt(e.control.value);
        p.update();

    }
    let gapSlider = new Slider({label: "Gap between items", min: 0, max: 50, step: 1, value: 0, showValue: true, onChange: gapSliderChange});
    
    function paddingSliderChange(e) {
        spacingStack.padding = e.control.value;
        p.update();
    }
    let paddingSlider = new Slider({label: "Stack padding", min: 0, max: 50, step: 1, value: 0, showValue: true, onChange: paddingSliderChange})

    let ids = await p.add([new Text({value: "Horizontal Stack - Gap and Padding", size: "xLarge"}), gapSlider, paddingSlider, spacingStack]);
    console.log("ids: ", ids);

    // wrapping
    let wrapStack = new Stack({horizontal: true, wrap: true, bgcolor: bgColor, gap: 20, childControls: [...items(10)]});
    function wrapSliderChange(e) {
        let width = parseInt(e.control.value);
        console.log("width from slider event: ", width);
        wrapStack.width = `${width}%`;
        p.update();
    }
    let wrapSlider = new Slider({label: "Change the stack width to see how child items wrap onto multiple rows", 
        min: 0, max: 100, step: 10, value: 100, showValue: true, valueFormat: "{value}%", onChange: wrapSliderChange
    })
    await p.add([new Text({value: "Horizontal Stack - Wrapping", size: "xLarge"}), wrapSlider, wrapStack]);

    // horizontal stack
    await p.add([
        new Text({value: "Horizontal stack - Horizontal Alignments", size: 'xLarge'}),
        createHorizontalStack("start"),    
        createHorizontalStack("center"),        
        createHorizontalStack("end"),
        createHorizontalStack("space-between"),        
        createHorizontalStack("space-around"),
        createHorizontalStack("space-evenly"),
        new Text({value: 'start'}),
        new Text({value: "Horizontal stack - Vertical Alignments", size: 'xLarge'}),
        new Stack({horizontal: true, verticalAlign:'start', height: 100, bgcolor: bgColor, gap: 20, childControls: [...items(3)]}),
        new Text({value: 'center'}),
        new Stack({horizontal: true, verticalAlign: 'center', height: 100, bgcolor: bgColor, gap: 20, childControls: [...items(3)]}),
        new Text({value: 'end'}),
        new Stack({horizontal: true, verticalAlign: 'end', height: 100, bgcolor: bgColor, gap: 20, childControls: [...items(3)]})
    ])

    // vertical stack
    await p.add([
        new Text({value: "Vertical stack - Vertical Alignments", size: 'xLarge'}),
        new Stack({horizontal: true, horizontalAlign: 'space-between', width: "100%", childControls: [
            createVerticalStack("start"),    
            createVerticalStack("center"),        
            createVerticalStack("end"),
            createVerticalStack("space-between"),        
            createVerticalStack("space-around"),
            createVerticalStack("space-evenly")
        ]})       
    ])

    // Stack submit
    function stackOnSubmit(e) {
        let stack = e.control;
        stack.childControls.unshift(new Message({value: "Form has been submitted!", type: "success", dismiss: true}))
        p.update();
    }
    let form1 = new Stack({padding: 10, width: '50%', border: '2px solid #eee', borderRadius: 5, childControls: [
        new Text({value: "Pressing ENTER inside the stack will fire 'submit' event."}),
        new Textbox({value: "First name"}),
        new Textbox({value: "Last name"})
    ], onSubmit: stackOnSubmit})

    await p.add([new Text({value: "Stack with submit event", size: "xLarge"}), form1]);

}

pglet.app("node-stack", main);