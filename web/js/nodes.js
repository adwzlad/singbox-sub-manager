async function getNodes(){


    try {


        const data = await apiFetch(

            "/nodes"

        );



        showResult(

            JSON.stringify(

                data,

                null,

                2

            )

        );



    } catch(e) {


        showResult(

            e.message

        );

    }

}









async function getNodeCount(){


    try {


        const data = await apiFetch(

            "/nodes/count"

        );



        showResult(

            JSON.stringify(

                data,

                null,

                2

            )

        );



    } catch(e) {


        showResult(

            e.message

        );

    }

}
