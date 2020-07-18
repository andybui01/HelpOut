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
    const{listings, adminRemoveListing} = props
    return(
    <>
    <ListHeader />
    <ListBody listings = {listings} adminRemoveListing={adminRemoveListing} />
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
                <th>{row.generalLocation}</th>
            </tr>
            <tr>
                <td colspan="2">{row.desc}</td>
            </tr>
            <tr>
                <td>
                    <button>Help out person name</button>
                </td>
                <td>
                    <button onClick={()=> props.adminRemoveListing(index)}> Delete Listing </button>
                </td>
            </tr>
        </>)
        })
    return (
        <lbody>{listRows}</lbody>
    )
}

export default ListView
