class Node {
  constructor(v) {
    this.v = v;
    this.next = null;
    this.prev = null;
  }
}

class Deque {
  constructor() {
    this.front = null;
    this.back = null;
    this.count = 0;
  }

  push(v) {
    const node = new Node(v);

    if (this.count === 0) {
      this.front = node;
      this.back = node;
    } else {
      const temp = this.back;
      temp.next = node;
      node.prev = temp;
      this.back = node;
    }
    this.count++;
    return;
  }

  pop() {
    if (this.count === 0) return null;

    const v = this.front.v;
    if (this.count === 1) {
      this.front = null;
      this.back = null;
    } else {
      this.front = this.front.next;
      this.front.prev = null;
    }
    this.count--;

    return v;
  }
}
function solution(queue1, queue2) {
  var answer = 0;
  let q1Sum = queue1.reduce((a, b) => a + b);
  let q2Sum = queue2.reduce((a, b) => a + b);

  if (q1Sum === q2Sum) return 0;
  else if ((q1Sum + q2Sum) % 2) return -1;

  const goal = (q1Sum + q2Sum) / 2;
  const q1 = new Deque();
  const q2 = new Deque();
  for (let node of queue1) {
    q1.push(node);
  }
  for (let node of queue2) {
    q2.push(node);
  }

  while (q1Sum !== q2Sum) {
    let nodeValue;

    if (q1Sum < goal) {
      nodeValue = q2.pop();
      if (nodeValue > goal) return -1;
      q1.push(nodeValue);

      q2Sum -= nodeValue;
      q1Sum += nodeValue;
    } else if (q1Sum > goal) {
      nodeValue = q1.pop();
      if (nodeValue > goal) return -1;
      q2.push(nodeValue);

      q1Sum -= nodeValue;
      q2Sum += nodeValue;
    }

    answer += 1;
    if (answer > 2 * 2 * queue1.length) return -1;
  }

  return answer;
}
