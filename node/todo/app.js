"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const pglet_1 = require("@britzkopf/pglet");
class Task {
    constructor(app, name) {
        this.app = app;
        this.displayTask = new pglet_1.Checkbox({ value: false, label: name, onChange: this.statusChanged.bind(this) });
        this.editName = new pglet_1.Textbox({ width: "100%" });
        this.displayView = new pglet_1.Stack({ horizontal: true, horizontalAlign: "space-between", verticalAlign: "center", childControls: [
                this.displayTask,
                new pglet_1.Stack({ horizontal: true, gap: "0", childControls: [
                        new pglet_1.Button({ icon: "Edit", title: "Edit Todo", onClick: this.editClicked.bind(this) }),
                        new pglet_1.Button({ icon: "Delete", title: "Delete Todo", onClick: this.deleteClicked.bind(this) })
                    ] })
            ] });
        this.editView = new pglet_1.Stack({ visible: false, horizontal: true, horizontalAlign: "space-between", verticalAlign: "center", childControls: [
                this.editName,
                new pglet_1.Button({ text: "Save", onClick: this.saveClicked.bind(this) })
            ] });
        this.view = new pglet_1.Stack({ childControls: [this.displayView, this.editView] });
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
    constructor(page) {
        this.page = page;
        this.tasks = [];
        this.newTask = new pglet_1.Textbox({ placeholder: "What needs doing?", width: "100%" });
        this.tasksView = new pglet_1.Stack({});
        this.filter = new pglet_1.Tabs({ value: "all", onChange: this.tabsChanged.bind(this), tabs: [
                new pglet_1.Tab({ text: "all" }), new pglet_1.Tab({ text: "active" }), new pglet_1.Tab({ text: "completed" })
            ] });
        this.itemsLeft = new pglet_1.Text({ value: "0 items left" });
        this.view = new pglet_1.Stack({ width: '70%', childControls: [
                new pglet_1.Text({ value: "Todos", size: "large", align: "center" }),
                new pglet_1.Stack({ horizontal: true, childControls: [
                        this.newTask,
                        new pglet_1.Button({ primary: true, text: 'Add', onClick: this.addClicked.bind(this) })
                    ] }),
                new pglet_1.Stack({ gap: '25', childControls: [
                        this.filter,
                        this.tasksView,
                        new pglet_1.Stack({ horizontal: true, horizontalAlign: "space-between", verticalAlign: "center", childControls: [
                                this.itemsLeft,
                                new pglet_1.Button({ text: "Clear completed", onClick: this.clearClicked.bind(this) })
                            ] })
                    ] })
            ] });
    }
    async update() {
        let status = this.filter.value;
        let count = 0;
        this.tasks.forEach(task => {
            task.view.visible = (status == 'all' ||
                (status == 'active' && task.displayTask.value == false) ||
                (status == 'completed' && task.displayTask.value == true));
            if (task.displayTask.value == false) {
                count++;
            }
        });
        this.itemsLeft.value = `${count} active items left`;
        await this.view.update();
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
        // //This approach won't work because of array iterator specification?
        // this.tasks.forEach(async task => {
        //     if (task.displayTask.value == true) {
        //         await this.deleteTask(task);
        //     }
        // })
        for (const task of this.tasks.filter(task => task.displayTask.value == true)) {
            await this.deleteTask(task);
        }
    }
}
async function main(page) {
    page.title = "ToDo app";
    page.horizontalAlign = 'center';
    await page.update();
    let app = new TodoApp(page);
    page.add([app.view]);
}
pglet_1.serveApp(main, { pageName: "ToDo App", web: false, noWindow: false });
