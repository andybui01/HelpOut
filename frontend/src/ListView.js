import React, {Component} from 'react'
/*
class ListView extends Component{
    render() {
        const {listings} = this.props

        return(
            <>
            <ListHeader />
            <ListBody listings={listings}/>
            </>
        )
    }
}*/

const ListView = (props) => {
    const{listings/*, adminRemoveListing*/} = props
    return(
    <>
    <ListHeader />
    <ListBody listings = {listings}/* adminRemoveListing={adminRemoveListing}*/ />
    </>
    )
}


const ListHeader = () => {
    return (
        <div className="ListHeader"> Requests for help near you </div>
    )
}

const ListBody = (props) => {
        const listRows = props.listings.map((row, index) => {
        return (<>
            <tr key={index}>
                <th>{row.title}</th>
                <th>{row.location}</th>
            </tr>
            <tr>
                <td colSpan="2">{row.desc}</td>
            </tr>
            <tr>
                <td colSpan="2">
                    <button>Help out person name</button>
                </td> 
            </tr>
        </>)
        })
    return (
        <table><tbody>{listRows}</tbody></table>
    )
}

export default ListView
