window.onload = (event) => {
    const currentTodoData = document.querySelector('#currentTodoData')
    const jsonTodoData = JSON.parse(JSON.parse(currentTodoData.innerText))
    displayTodos(jsonTodoData, false)
};

const todoCompletedLink = document.querySelector('#todoCompleted')
const todoActiveLink = document.querySelector('#todoActive')

todoCompletedLink.addEventListener('click', async function (e) {
    removeTodos();
    const completedTodosUrl = document.getElementById("completedTodosUrl").href;
    const res = await axios.get(completedTodosUrl)
    console.log(res.data)
    const completedTodos = JSON.parse(res.data.completedtodos);
    displayTodos(completedTodos, true)
})

todoActiveLink.addEventListener('click', async function (e) {
    removeTodos();
    console.log('Hello?')
    const currentTodoData = document.querySelector('#currentTodoData')
    const jsonTodoData = JSON.parse(JSON.parse(currentTodoData.innerText))
    displayTodos(jsonTodoData, false)
})

const removeTodos = () => {
    const todoItems = document.querySelector('#todoItems')
    for (let item of Array.from(todoItems.children)) {
        item.remove()
    }
}

const displayTodos = (todos, isCompleted) => {
    for (let item of todos) {
        //<div class="input-group mb-2">
        const divInputGroup = document.createElement('div');
        divInputGroup.setAttribute('class', 'input-group mb-2');
        //<textarea class="form-control" readonly>dummy data</textarea>
        const textAreaFormControl = document.createElement('textarea');
        textAreaFormControl.setAttribute('class', 'form-control');
        textAreaFormControl.readOnly = true;
        if(item.fields.memo === ""){
            textAreaFormControl.value = `${item.fields.title} - ${item.pk}`
        }else{
            textAreaFormControl.value = `${item.fields.title} - ${item.fields.memo} - ${item.pk}`
        }
        //<button class="btn btn-success" type="button">Complete</button>
        const completeButton = document.createElement('button');
        completeButton.setAttribute('class', 'btn btn-success');
        completeButton.setAttribute('type', 'button');
        completeButton.textContent = 'Complete'
        //<button class="btn btn-danger" type="button">Delete</button>
        const deleteButton = document.createElement('button');
        deleteButton.setAttribute('class', 'btn btn-danger');
        deleteButton.setAttribute('type', 'button');
        deleteButton.textContent = 'Delete';
        //Active todos require both complete and delete button
        divInputGroup.appendChild(textAreaFormControl);
        if(isCompleted){
            divInputGroup.appendChild(deleteButton);
        }else{
            divInputGroup.appendChild(completeButton);
            divInputGroup.appendChild(deleteButton);
        }
        document.getElementById('todoItems').appendChild(divInputGroup)
    }
}