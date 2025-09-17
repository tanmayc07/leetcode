function calPoints(operations: string[]): number {
    let st = [];

    for (let i=0; i<operations.length; i++) {
        if (!isNaN(Number(operations[i]))) 
            st.push(Number(operations[i]))
        else if (operations[i] === '+') {
            let p1 = st.pop();
            let p2 = st.pop();
            let res = p1+p2;
            st.push(p2);
            st.push(p1);
            st.push(res);
        } else if (operations[i] === 'D')
            st.push(st[st.length-1] * 2);
        else if (operations[i] === 'C')
            st.pop();
    }

    return st.reduce((acc, curr) => curr+acc, 0);
};