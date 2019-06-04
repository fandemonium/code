1. search for data desired here: `https://data.neonscience.org/static/browse.html`

2. get the product ID, eg. soil microbe community composition is `DP1.10081.001`

3. got to R and pull all urls linked to the product id. The expanded table contains sample/DNA id and sra prj numbers. many if not all sequences are in mgrast. mgrast sequence download requires mgm numbers. 

4. download all mgrast neon associated information: `http://api.metagenomics.anl.gov/search?all=neon&limit=1000`
	+ default limit is 10. in the browser, one can set limit to 1000. but using wget or curl, the limit is 10, regardless of what number you supply. 
	+ the next set of url are at the bottom of the returned json. use web browser, set 1000, copy the pastes. 


