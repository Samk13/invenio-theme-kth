 class MyComponent extends Component{
    render(){
        return "Hello World!"
    }
}


const domContainer = document.getElementById("invenio-details-config");
domContainer &&
  ReactDOM.render(
    <MyCustomComponent />,
    domContainer
  );