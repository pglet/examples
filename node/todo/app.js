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
    async update() {
        let status = this.filter.value;

        let count = 0;
        this.tasks.forEach(task => {
            //console.log("task.displayTask.value: ", task.displayTask.value);
            //console.log("status: ", status);
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
                count++;
            } 
        })
        this.itemsLeft.value = `${count} active items left`
        await this.view.update()
    }

    addClicked(e) {
        let task = new Task(this, this.newTask.value);
        this.tasks.push(task);
        this.tasksView.childControls.push(task.view);
        this.newTask.value = "";
        this.update();
    }

    async deleteTask(task) {
        //console.log("task in delteTask: ", task)
        let index = this.tasks.indexOf(task);
        if (index > -1) {
            this.tasks.splice(index, 1);
        } 
        let index2 = this.tasksView.childControls.indexOf(task.view);
        if (index2 > -1) {
            this.tasksView.childControls.splice(index, 1);
        } 

        await this.update();
    }

    tabsChanged(e) {
        this.update();
    }

    async clearClicked(e) {
        // //This approach doesn't work because of array iterator specification?
        // this.tasks.forEach(task => {
        //     //console.log("taskview from foreach: ", task.view)
        //     if ((task.displayTask.value == true) || (task.displayTask.value == "true")) {
        //         this.deleteTask(task);
        //     }
        // })
        // this.tasks.filter(task => {
        //     let cond = task.displayTask.value == true || task.displayTask.value == "true"
        //     if (cond) {
        //         this.deleteTask(task);
        //     }
        //     return cond;
        // })
        for (let i = this.tasks.length - 1; i >= 0; i--) {
            if (this.tasks[i].displayTask.value == true || this.tasks[i].displayTask.value == "true"){
                await this.deleteTask(this.tasks[i]);
            }
        }
        // console.log("this.tasks final: ", this.tasks);
        // console.log("this.tasksView.childControls final: ", this.tasksView.childControls);
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