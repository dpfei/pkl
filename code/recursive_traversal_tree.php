<?php

// 这是一个递归遍历树的程序
// 在这里我先提供一个N棵树的数据结构。这棵树有N个根节点，有无限层中间节点和叶子节点。在每个节点中存在的元素为：id，name，children。
// 实现的算法中要求，根据给出的id查找出此id所在路径上的所有name并返回。
/*
[
    {
        "id": 1,
        "name": "图书",
        "children": [
            {
                "id": 2,
                "name": "四书",
                "children": [
                    {
                        "id": 3,
                        "name": "大学"
                    },
                    {
                        "id": 4,
                        "name": "中庸"
                    },
                    {
                        "id": 5,
                        "name": "论语"
                    },
                    {
                        "id": 6,
                        "name": "孟子"
                    }
                ]
            },
            {
                "id": 7,
                "name": "五经",
                "children": [
                    {
                        "id": 8,
                        "name": "诗经"
                    },
                    {
                        "id": 9,
                        "name": "礼记"
                    },
                    {
                        "id": 10,
                        "name": "周易"
                    },
                    {
                        "id": 11,
                        "name": "春秋"
                    }
                ]
            }
        ]
    }
]
*/
function search($treeData, $num)
{
    $resArr = [];
    foreach ($treeData as $v) {
        if ($v['id'] == $num) {
            $resArr[] = $v['name'];
            break;
        } else {
            if (isset($v['children'])) {
                $resArr = search($v['children'], $num);
                if (!empty($resArr)) {
                    array_unshift($resArr, $v['name']);
                    break;
                }
            }
        }
    }
    return $resArr;
}

$treeData = '[{"id":1,"name":"图书","children":[{"id":2,"name":"四书","children":[{"id":3,"name":"大学"},{"id":4,"name":"中庸"},{"id":5,"name":"论语"},{"id":6,"name":"孟子"}]},{"id":7,"name":"五经","children":[{"id":8,"name":"诗经"},{"id":9,"name":"礼记"},{"id":10,"name":"周易"},{"id":11,"name":"春秋"}]}]}]';
$treeArr = json_decode($treeData, true);
$searchResult = search($treeArr, 10);
print_r($searchResult);