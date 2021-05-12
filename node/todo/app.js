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
        this.displayTask = new Checkbox({value: false, label: name, onChange: this.statusChanged.bind(this)});
        this.editName = new Textbox({width: "100%"});
        this.displayView = new Stack({horizontal: true, horizontalAlign: "space-between", verticalAlign: "center", childControls: [
            this.displayTask,
            new Stack({horizontal: true, gap: "0", childControls: [
                new Button({icon: "Edit", title: "Edit Todo", onClick: this.editClicked.bind(this)}),
                new Button({icon: "Delete", title: "Delete Todo", onClick: this.deleteClicked.bind(this)})
            ]})
        ]})
        this.editView = new Stack({visible: false, horizontal: true, horizontalAlign: "space-between", verticalAlign: "center", childControls: [
            this.editName,
            new Button({text: "Save", onClick: this.saveClicked.bind(this)})
        ]})
        this.view = new Stack({childControls: [this.displayView, this.editView]})
    }

    editClicked(e) {
        this.editName.value = this.displayTask.label;
        this.displayView.visible = false;
        this.editView.visible = true;
        this.view.update();
    }
    saveClicked(e) {
        this.displayView.label = this.editName.value;
        this.displayView.visible = true;
        this.editView.visible = false;
        this.view.update();
    }
    deleteClicked(e) {
        this.app.deleteTask();
    }
    statusChanged(e) {
        this.app.update();
    }
}
class TodoApp {
    constructor(page) {
        this.page = page;
        this.tasks = [];
        this.newTask = new Textbox({placeholder: "What needs doing?", width: "100%"});
        this.tasksView = new Stack({});
        this.filter = new Tabs({value: "all", onChange: this.tabsChanged.bind(this), tabs: [
            new Tab({text: "all"}), new Tab({text: "active"}), new Tab({text: "completed"})
        ]})
        this.itemsLeft= new Text({value: "0 items left"})
        this.view = new Stack({ width: '70%', childControls: [
            new Text({value: "Todos", size: "large", align: "center"}),
            new Stack({ horizontal: true, childControls: [
                this.newTask,
                new Button({primary: true, text: 'Add', onClick: this.addClicked.bind(this)})
            ] }),
            new Stack({gap: 25, childControls: [
                this.filter,
                this.tasksView,
                new Stack({horizontal: true, horizontalAlign: "space-between", verticalAlign: "center", childControls: [
                    this.itemsLeft,
                    new Button({text: "Clear completed", onClick: this.clearClicked.bind(this)})
                ]})
            ]})
        ] });
    }
    update() {
        //console.log("Update Runs!!!")
        let status = this.filter.value;
        //console.log("status: ", status);
        let count = 0;
        this.tasks.forEach(task => {
            console.log("task.displayTask.value: ", task.displayTask.value);
            console.log("status: ", status);
            // task.view.visible = (status == 'all' || 
            //         (status == 'active' && task.displayTask.value == false) || 
            //         (status == 'completed' && task.displayTask.value == true))
            // if ((status == "all") || (status == "active" && task.displayTask.value == false) || (status == "completed" && task.displayTask.value == true)) {
            //     task.view.visible = true;
            // }
            // else {
            //     task.view.visible = false;
            // }
            if (status == "all") {
                task.view.visible = true;
            }
            else if (status == "active" && ((task.displayTask.value == false) || (task.displayTask.value == "false"))) {
                task.view.visible = true;
            }
            else if (status == "completed" && ((task.displayTask.value == true) || (task.displayTask.value == "true"))) {
                task.view.visible = true;
            }
            else {
                task.view.visible = false;
            }
            if ((task.displayTask.value == false) || (task.displayTask.value == "false")) {
                console.log("count increment");
                count++;
            } 
        })
        console.log("count: ", count);
        this.itemsLeft.value = `${count} active items left`
        this.view.update()
    }
    addClicked(e) {
        let task = new Task(this, this.newTask.value);
        this.tasks.push(task);
        //let taskValue = this.newTask.value //await this.page.getValue(this.newTask); //
        //let checkBox = new Checkbox({value: false, label: taskValue});
        this.tasksView.childControls.push(task.view);
        this.newTask.value = "";
        this.update();
    }
    deleteTask(task) {
        let index = this.tasks.indexOf(task);
        if (index > -1) {
            this.tasks.splice(index, 1);
        } 
        this.tasksView.childControls = this.tasksView.childControls.filter(ctrl => ctrl != task.view);
        this.update();
    }
    tabsChanged(e) {
        this.update();
    }
    clearClicked(e) {
        this.tasks.forEach(task => {
            if (task.displayTask.value == true) {
                this.deleteTask(task);
            }
        })
    }

}

async function main(page) {
    page.title = "ToDo app";
    page.horizontalAlign = 'center';
    await page.update();
    let app = new TodoApp(page);
    page.add([app.view]);

}

pglet.app("TodoApp", main);