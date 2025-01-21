import React, {useState, useEffect} from 'react'


const Todo = () => {
    const [todos, setTodos] = useState([])
    const [newTodo, setNewTodo] = useState("")

    // fetching Todos
    const fetchTodo = async () =>{
        try {
            const response = await fetch('http://127.0.0.1:8000/api/todo/')
            if (response.ok) {
                const data = await response.json()
                setTodos(data);
            }else{
                console.log("Error while fetching todos :", response.statusText);
            }
        } catch (error) {
            console.log("Error while fetching todos :", );
            
        }
    }

    // Adding New Todo
    const addTodo = async ()=>{
        try {
            const response = await fetch("http://127.0.0.1:8000/api/todo/",{
                method : 'POST',
                headers : {
                    "Content-Type": "application/json",
                },
                body : JSON.stringify({todo: newTodo, isCompleted: false})
            });
            if(response.ok){
                const newTodoData = response.json()
                setTodos([...todos,newTodoData])
                setNewTodo("")
                fetchTodo();
            }
            else{
                console.log('error while adding a todo : ', response.statusText);
                
            }
        } catch (error) {
            console.log("error while adding a todo : ", error);
            
        }
    } 

    // toggling isCompleted Todo
    const isCompleted = async (id, isCompleted)=>{
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/todo/${id}/`,{
                method : 'PATCH',
                headers : {
                    "Content-Type": "application/json",
                },
                body : JSON.stringify({ isCompleted: !isCompleted})
            });
            if(response.ok){
                fetchTodo()
            }else{
                console.log('error while toggling isCompleted : ', response.statusText);
                
            }
        } catch (error) {
            console.log("error while adding a todo : ", error);
            
        }
    } 
// Delete a todo
const deleteTodo = async (id) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/todo/${id}/`, {
            method: "DELETE",
        });

        if (response.ok) {
            // Successfully deleted, update state
            setTodos(todos.filter((todo) => todo.id !== id));
            fetchTodo();
        } else {
            // Handle non-OK responses
            try {
                const errorData = await response.json();
                console.log("Error details:", errorData);
            } catch (err) {
                console.log("Error parsing JSON response:", err);
                console.log("Raw response:", await response.text());
            }
        }
    } catch (error) {
        // Handle fetch errors
        console.log("Error while deleting:", error);
    }
};

    // handle submit
    const handleSubmit =(e)=>{
        e.preventDefault()
    }

    // fetch todo when component mounts
    useEffect(() => {
     fetchTodo();
    }, [])
    

  return (
    <>
        <div className='p-5 flex justify-center flex-col items-center text-white'>
            <h1 className='text-xl my-3'>Todos</h1>
            <form onSubmit={handleSubmit} className='flex flex-col gap-2 items-center' >

            <input type="text"
                className='bg-gray-700 p-1 text-white border-none outline-none mb-2'
                value={newTodo}
                onChange={(e)=>setNewTodo(e.target.value)}
                placeholder='add a todo'
            />
            <button
                className='bg-red-500 p-1 rounded-md'
                onClick={()=>{addTodo()}}
            >
                ADD TODO
            </button>
            </form>
            <h3 className='text-2xl m-2'>Your Todos</h3>
            <ul>
                {todos.map((todo)=>(
                    <li key={todo.id} className='m-1 text-sm text-gray-300 flex gap-2 justify-between '>
                        <input
                            className=" text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"
                            type='checkbox'
                            checked = {todo.isCompleted}
                            onChange = {()=> isCompleted(todo.id, todo.isCompleted)}
                        />
                        <span className='text-xl'>
                            {todo.todo}
                        </span>
                        <button
                            className='bg-green-600 px-1 text-[12px] rounded-lg'
                            onClick={()=>deleteTodo(todo.id)}
                        >Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    </>
  )
}

export default Todo