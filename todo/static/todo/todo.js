const todoCompletedLink = document.querySelector('#todoCompleted')
const todoActiveLink = document.querySelector('#todoActive')

todoCompletedLink.addEventListener('click', async function (e) {
    removeTodos();
    const completedTodosUrl = document.getElementById("completedTodosUrl").href;
    const res = await axios.get(completedTodosUrl)
    console.log(res.data)
    displayCompletedTodos(res.data)

})

const removeTodos = () => {
    const todoItems = document.querySelector('#todoItems')
    for (let item of Array.from(todoItems.children)) {
        item.remove()
    }
}

const displayCompletedTodos = (completedTodos) => {
    for (let item of JSON.parse(completedTodos.completedtodos)) {
        //<div class="input-group mb-2">
        const divInputGroup = document.createElement('div');
        divInputGroup.setAttribute('class', 'input-group mb-2');
        //<textarea class="form-control" readonly>dummy data</textarea>
        const textAreaFormControl = document.createElement('textarea');
        textAreaFormControl.setAttribute('class', 'form-control');
        textAreaFormControl.readOnly = true;
        if(item.fields.memo === ""){
            textAreaFormControl.value = `${item.fields.title}`
        }else{
            textAreaFormControl.value = `${item.fields.title} - ${item.fields.memo}`
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
        divInputGroup.appendChild(textAreaFormControl);
        //divInputGroup.appendChild(completeButton);
        divInputGroup.appendChild(deleteButton);
        document.getElementById('todoItems').appendChild(divInputGroup)
    }

}




// todoCompletedLink.addEventListener('click', async function (e) {
//     e.preventDefault();
//     console.log(todoCompletedLink)
//     removeCompletedTodos(document.querySelectorAll('#movies p'));
//     const completedTodosUrl = document.getElementById("completedTodosUrl").href;
//     const res = await axios.get(completedTodosUrl)
//     displayCompletedTodos(res.data)
// })

// const removeCompletedTodos = (completedTodos) => {
//     for (let item of completedTodos) {
//         item.remove();
//     }
// }

// const displayCompletedTodos = (completedTodos) => {
//     for (let item of JSON.parse(completedTodos.completedtodos)) {
//         const paragraph = document.createElement('p');
//         paragraph.innerText = item.fields.title
//         const divMovies = document.querySelector('#movies');
//         divMovies.append(paragraph)
//     }
// }


// const mydata = JSON.parse(document.getElementById('mydata').textContent);
// const obj = JSON.parse(mydata)

// const form = document.querySelector('#searchForm');
// form.addEventListener('submit', async function (e) {
//     e.preventDefault();
//     removeCompletedTodos(document.querySelectorAll('#movies p'));
//     const completedTodosUrl = document.getElementById("completedTodosUrl").href;
//     const res = await axios.get(completedTodosUrl)
//     displayCompletedTodos(res.data)
// })

// const removeCompletedTodos = (completedTodos) => {
//     for (let item of completedTodos) {
//         item.remove();
//     }
// }

// const displayCompletedTodos = (completedTodos) => {
//     for (let item of JSON.parse(completedTodos.completedtodos)) {
//         const paragraph = document.createElement('p');
//         paragraph.innerText = item.fields.title
//         const divMovies = document.querySelector('#movies');
//         divMovies.append(paragraph)
//     }
// }