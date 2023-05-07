# React---Filter举例

index.js  
```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
    <App />,
  document.getElementById('root')
);
```

App.js  
```js
import React from 'react';
import {useState} from 'react'
import './App.css';
import Filter from './components/Filter'

function App() {
  const [filterValue, setFilterValue] = useState('')

  const handleFilterValueChange = (event) => {
    console.log(event.target.value)
    setFilterValue(event.target.value)
  }

  return (
    <div>
      <Filter filterValue={filterValue} handleFilterValueChange={handleFilterValueChange} />
    </div>
  );
}

export default App;
```

Filter.js  
```js
import React from 'react'

const Filter = (props) =>
 <div>find countries <input value={props.filterValue} onChange={props.handleFilterValueChange} /></div>

export default Filter
```


2020/8/18  
