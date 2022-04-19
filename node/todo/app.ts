import { serveApp, Page, Control, Text, Stack, Textbox, Button, Tab, Tabs, Checkbox } from '@britzkopf/pglet';
//import { serveApp, Page, Control, Text, Stack, Textbox, Button, Tab, Tabs, Checkbox } from 'https://deno.land/x/pglet@v0.1.8/index.ts';

class Task {
    app?: TodoApp;
    displayTask?: Checkbox;
    editName?: Textbox;
    displayView?: Stack;
    editView?: Stack;
    view?: Stack;

    constructor(app: TodoApp, name: string) {
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
        this.displayTask.label = this.editName.value;
        this.displayView.visible = true;
        this.editView.visible = false;
        this.view.update();
    }

    deleteClicked(e) {
        this.app.deleteTask(this);
    }

    statusChanged(e) {
        this.app.update();
    }

}
class TodoApp {
    page?: Control;
    tasks?: Task[];
    newTask?: Textbox;
    tasksView?: Stack;
    filter?: Tabs;
    itemsLeft?: Text;
    view?: Stack;

    constructor(page: Page) {
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
            new Stack({gap: '25', childControls: [
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
            task.view.visible = (status == 'all' || 
                    (status == 'active' && task.displayTask.value == false) || 
                    (status == 'completed' && task.displayTask.value == true))
            
            if (task.displayTask.value == false) {
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
        let i = this.tasks.indexOf(task);
        if (i > -1) {
            this.tasks.splice(i, 1);
        } 
        
        let j = this.tasksView.childControls.indexOf(task.view);
        if (j > -1) {
            this.tasksView.childControls.splice(j, 1);
        } 

        await this.update();
    }

    tabsChanged(e) {
        this.update();
    }

    async clearClicked(e) {
        for (const task of this.tasks.filter(task => task.displayTask.value == true)) {
            await this.deleteTask(task);
        }     
    }

}

async function main(page: Page) {
    page.title = "ToDo app";
    page.horizontalAlign = 'center';
    await page.update();
    let app = new TodoApp(page);
    page.add([app.view]);
}

serveApp(main, {pageName: "ToDo App", web: false, noWindow: false});
