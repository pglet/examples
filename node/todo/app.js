const pglet = require('../../../pglet-node/build/index.js');

const Text = pglet.Text;
const Stack = pglet.Stack;
const Textbox = pglet.Textbox;
const Button = pglet.Button;
const Checkbox = pglet.Checkbox;
const Tabs = pglet.Tabs;
const Tab = pglet.Tab;


class Task {
    constructor(app, name) {
        this.app = app;
        this.displayTask = new Checkbox({value: false, label: name, onChange: this.statusChanged});
        this.editname = Textbox()
    }
}
class TodoApp {
    constructor(page) {
        this.page = page;
        this.newTask = new Textbox({placeholder: "What needs doing?", onchange: true});
        this.tasksView = new Stack({});
        this.view = new Stack({ width: '70%', childControls: [
            new Stack({ horizontal: true, childControls: [
                this.newTask,
                new Button({text: 'Add', onClick: this.addClicked.bind(this)})
            ] }),
            this.tasksView
        ] });
    }
    async addClicked(e) {
        let taskValue = await this.page.getValue(this.newTask); //this.newTask.value 
        let checkBox = new Checkbox({value: false, label: taskValue});
        this.tasksView.childControls.push(checkBox);
        this.page.update();
    }
}

async function main(page) {
    page.title = "ToDo app";
    page.horizontalAlign = 'center';
    await page.update();
    let app = new TodoApp(page);
    page.add([app.view]);

}

pglet.app("todo-app", main);