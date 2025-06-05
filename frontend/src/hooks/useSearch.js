import { useState, useCallback } from 'react';
import { searchCompanies } from '../services/companyService';

/**
 * Custom hook for searching companies
 * 
 * @returns {Object} The search state and functions
 */
const useSearch = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [results, setResults] = useState({ count: 0, companies: [] });
  const [query, setQuery] = useState('');
  const [page, setPage] = useState(0);
  const limit = 10;

  const search = useCallback(async (searchQuery, pageNumber = 0) => {
    if (!searchQuery.trim()) {
      return;
    }

    setIsLoading(true);
    setError(null);
    setQuery(searchQuery);
    setPage(pageNumber);

    try {
      const offset = pageNumber * limit;
      const data = await searchCompanies(searchQuery, limit, offset);
      setResults(data);
    } catch (err) {
      setError(err.message || 'An error occurred while searching');
      console.error('Search error:', err);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const nextPage = useCallback(() => {
    if (results.count > (page + 1) * limit) {
      search(query, page + 1);
    }
  }, [search, query, page, results.count]);

  const previousPage = useCallback(() => {
    if (page > 0) {
      search(query, page - 1);
    }
  }, [search, query, page]);

  return {
    isLoading,
    error,
    results,
    query,
    page,
    limit,
    search,
    nextPage,
    previousPage,
    hasNextPage: results.count > (page + 1) * limit,
    hasPreviousPage: page > 0
  };
};

export default useSearch; 