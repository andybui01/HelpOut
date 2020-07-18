import React, {Component} from 'react'
/*
		request.form.get('personID'),
		request.form.get('title'),
		request.form.get('desc'),
		request.form.get('commitment'),
		request.form.get('location')
*/
const ReachOut = () => {
    return(
    <>
    <form action="http://127.0.0.1:5000/listing/create" method="POST">
        <label htmlFor="title">Title your request.</label>
        <input type="text" name="title" id="title" />
        
        <label htmlFor="desc">Describe your request.</label>
        <input type="text" name="desc" id="desc" />
        
        <label htmlFor="commitment">How long will you need?</label>
        <input type="text" name="commitment" id="commitment" />
        
        <label htmlFor="suburb">What suburb are you based?</label>
        <input type="text" name="suburb" id="suburb" />
        
        <div>
            <button> Submit </button>
        </div>
    </form>
    </>
    );
}

export default ReachOut
