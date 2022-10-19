const rc = (p, c) => {
  if (c?.items?.length) {
    return { ...p, [c.id]: c?.items?.reduce(rc, {}) };
  } else {
    return { ...p, [c.id]: { is_read_active: 1 } };
  }
};

const resultObj = data.reduce(rc, {});

setRObj(resultObj);
