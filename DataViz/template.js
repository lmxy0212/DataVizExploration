const originalData = {

}


// Transform the data
const transformedData = {
    nodes: originalData.nodes.map(node => ({
        id: node.id,
        name: node.name,
        val: node.val
    })),
    links: originalData.links.map(link => ({
        source: link.source,
        target: link.target
    }))
};

// Export the transformed data so it can be used in another script
window.transformedData = transformedData;
