import "./widget.scss"

const widget = ({type }) => {

  let data;
    switch(type){
      case "unresolved":
        data={
          title:"Unresolved",
          count:60,
        };
        break;
        case "new agreements":
        data={
          title:"New agreements",
          count:16,
        };
        break;
        case "finished":
        data={
          title:"Finished",
          count:436,
        };
        break;
        case "drafts":
        data={
          title:"Drafts",
          count:64,
        };
        break;
        default:
          break;
    }

  return (
    <div className="widget">
        <div className="content">
          <span className="title">{data.title}</span>
          <span className="count">{data.count}</span>
        </div>
        
    </div>
  )
}

export default widget