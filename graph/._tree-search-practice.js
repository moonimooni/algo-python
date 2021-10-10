function search(graph, parentDir, visited) {
  visited += [parentDir];
  graph[parentDir].forEach((childDir) => {
    if (!visited[childDir]) {
      search(graph, childDir, visited);
    }
  })
}

function solution(n, relation, dirname) {
  const tree = {};

  const dirnameWithN = dirname.map((e, i) => {
    return [e, i + 1];
  });

  dirnameWithN.forEach((e) => {
    tree[e] = [];
  });

  relation.forEach((e) => {
    const parentDir = dirnameWithN[e[0] - 1];
    const childDir = dirnameWithN[e[1] - 1];

    tree[parentDir].push(childDir);
  });
  search(tree, dirnameWithN[0], []);
}

console.log(
  solution(
    7,
    [
      [1, 2],
      [2, 5],
      [2, 6],
      [1, 3],
      [1, 4],
      [3, 7],
    ],
    ["root", "abcd", "cs", "hello", "etc", "hello", "solution"]
  )
);
