import { useState, useEffect } from 'react';
import {
  Drawer,
  DrawerBody,
  DrawerHeader,
  DrawerOverlay,
  DrawerContent,
  DrawerCloseButton,
  Box,
  Text,
  List,
  ListItem
} from '@chakra-ui/react';
import { TimeIcon } from '@chakra-ui/icons';
import LoadingSpinner from './LoadingSpinner';
import { formatRegNumber } from '../../utils/formatters';
import api from '../../services/api';

/**
 * SearchHistoryDrawer component - displays recent company searches
 * 
 * @param {boolean} isOpen - Whether the drawer is open
 * @param {function} onClose - Function to close the drawer
 * @param {function} onCompanySelect - Function to handle company selection
 * @returns {JSX.Element} SearchHistoryDrawer component
 */
const SearchHistoryDrawer = ({ isOpen, onClose, onCompanySelect }) => {
  const [searchHistory, setSearchHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
    const fetchSearchHistory = async () => {
      if (isOpen) {
        setIsLoading(true);
        try {
          const response = await api.get('/api/search-history');
          setSearchHistory(response.data || []);
        } catch (error) {
          console.error('Error fetching search history:', error);
        } finally {
          setIsLoading(false);
        }
      }
    };
    
    fetchSearchHistory();
  }, [isOpen]);
  
  return (
    <Drawer isOpen={isOpen} placement="right" onClose={onClose} size="md">
      <DrawerOverlay />
      <DrawerContent>
        <DrawerCloseButton />
        <DrawerHeader borderBottomWidth="1px">Recent Company Searches</DrawerHeader>
        <DrawerBody>
          {isLoading ? (
            <LoadingSpinner text="Loading search history..." />
          ) : searchHistory.length > 0 ? (
            <List spacing={3}>
              {searchHistory.map((item, index) => (
                <ListItem 
                  key={`${item.reg_number}-${index}`}
                  p={3}
                  borderWidth="1px"
                  borderRadius="md"
                  _hover={{ bg: 'gray.50', cursor: 'pointer' }}
                  onClick={() => {
                    onCompanySelect(item.reg_number);
                    onClose();
                  }}
                >
                  <Box>
                    <Text fontWeight="bold">{item.name}</Text>
                    <Text fontSize="sm" color="gray.600">
                      {formatRegNumber(item.reg_number)}
                    </Text>
                    <Text fontSize="xs" color="gray.500" mt={1}>
                      <TimeIcon mr={1} />
                      {new Date(item.search_time).toLocaleString()}
                    </Text>
                  </Box>
                </ListItem>
              ))}
            </List>
          ) : (
            <Text>No search history found.</Text>
          )}
        </DrawerBody>
      </DrawerContent>
    </Drawer>
  );
};

export default SearchHistoryDrawer; 