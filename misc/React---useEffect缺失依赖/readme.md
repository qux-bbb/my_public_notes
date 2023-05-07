# React---useEffect缺失依赖

源代码如下：  
```js
  const [weather, setWeather] = useState({})

  useEffect(() => {
    axios
      .get('http://api.weatherstack.com/current', {
        params: {
          access_key: api_key,
          query: country.capital
        }
      })
      .then(response => {
        setWeather(response.data.current)
      })
  }, [])
```

警告如下：  
```
React Hook useEffect has a missing dependency: 'country.capital'. Either include it or remove the dependency array  react-hooks/exhaustive-deps
```

解决方法就是在最后的中括号里加一个 country.capital，也就是：  
```
...
  }, [country.capital])
```

参考：  
https://stackoverflow.com/questions/55840294/how-to-fix-missing-dependency-warning-when-using-useeffect-react-hook  


2020/8/25  
